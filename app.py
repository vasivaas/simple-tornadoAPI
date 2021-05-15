import json
import pymongo
import tornado.httpserver
import tornado.ioloop
import tornado.escape
import tornado.options
from tornado.options import define, options
from tornado.web import RequestHandler
from typing import Union

from serializer_deserializer.encode.object_serializer import ObjectSerializer
from models.credential import ApiToken, UserPassword


define('mondodb_host', default='mongodb://localhost:27017', help='Main user DB')
define('port', default=8888, help='port to listen on', type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/api/v1/credentials", MainHandler),
            (r"/api/v1/credentials/(?P<credential_id>\w+)", MainHandler),
        ]

        settings = dict(
            debug=True,
        )

        self.con = pymongo.MongoClient(options.mondodb_host)
        self.database = self.con['users']
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(RequestHandler):
    def get(self, credential_id=None):
        if credential_id is None:
            credentials = self._database().find()
            return self.write({'credentials': list(credentials)})
        else:
            if (credential := self._find_by_id(credential_id)) is None:
                raise tornado.web.HTTPError(404)
            return self.write(credential)

    def post(self):
        params = json.loads(self.request.body)
        token_credential, user_password_credential = ApiToken(params), UserPassword(params)
        new_user_password_id = self._add_credential(user_password_credential)
        new_token_id = self._add_credential(token_credential)
        created_credentials = self._database().find({'$or': [{'_id': new_user_password_id, },
                                                                                  {'_id': new_token_id}]
                                                                          })
        self.set_status(201)
        self.write(json.dumps(list(filter(None, created_credentials))))

    def delete(self, credential_id):
        delete_credential = self._database().delete_one({"_id": credential_id})
        if delete_credential.deleted_count == 1:
            self.set_status(204)
            return self.finish()
        raise tornado.web.HTTPError(404)

    def _add_credential(self, credential_object: Union[ApiToken, UserPassword]) -> str:
        if credential_object.is_valid():
            credential_dict = ObjectSerializer().encode_object('JSON', credential_object)
            db_data = self._database().insert_one(credential_dict)
            return db_data.inserted_id
        return None

    def _find_by_id(self, credential_id: str) -> dict:
        return self._database().find_one({'_id': credential_id})

    def _database(self):
        return self.application.database.credentials


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
