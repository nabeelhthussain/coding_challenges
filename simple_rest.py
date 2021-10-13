#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 13:50:57 2021

@author: nabeelhussain

OUTPUT:
    
curl -XGET http://127.0.0.1:8080/company/LTX
{
    "company": "LTX",
    "views": 1000,
    "title": "Finance"
}

curl -XPOST http://127.0.0.1:8080/company/Apple -H "Content-Type: application/json"  --data '{ "company": "Apple", "views": "1199", "title": "Technology" }'
{
    "company": "Apple",
    "views": "1199",
    "title": "Technology"
}

curl -XGET http://127.0.0.1:8080/company/Apple
{
    "company": "Apple",
    "views": "1199",
    "title": "Technology"
}

"""

from flask import Flask
from flask_restful import Resource, reqparse ,Api


ap = Flask(__name__)
api = Api(ap)

companies = [
    {
        "company": "Broadridge",
        "views": 1000,
        "title": "Finance"
    },
    {
        "company": "LTX",
        "views": 1000,
        "title": "Finance"
    },
    {
        "company": "Google",
        "views": 3000,
        "title": "Technology"
    }
]

class Company(Resource):
    def get(self, company):
        for c in companies:
            if(company == c["company"]):
                return c, 200
        return "company not found", 404
    
    def post(self, company):
        parser = reqparse.RequestParser()
        parser.add_argument("views")
        parser.add_argument("title")
        args = parser.parse_args()

        for c in companies:
            if(company == c["company"]):
                return "company  {} already exists".format(company), 400

        c = {
            "company": company,
            "views": args["views"],
            "title": args["title"]
        }
        companies.append(c)
        return c, 201
    
api.add_resource(Company, "/company/<string:company>")

ap.run(debug=True,port=8080)