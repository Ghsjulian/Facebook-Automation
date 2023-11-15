"use strict";

class XHR {
    constructor() {
        this.developer = "Ghs Julian";
        this.email = "ghsjulian@gmail.com";
        this.contact = "fb/ghs.julian.85";
    }
    get(getData = {}) {
        if (typeof getData === "object") {
            try {
                /* code */
                var req = new XMLHttpRequest();
                req.responseType = "json";
                req.open("GET", getData.url, true);
                req.onload = function () {
                    var response = req.response;
                    getData.getAction(response);
                };
                req.send(null);
            } catch (e) {
                console.warn("Error : " + e);
            }
        } else {
            console.warn("Please Send An Object!");
        }
    }

    delete(getData = {}) {
        if (typeof getData === "object") {
            try {
                /* code */
                var req = new XMLHttpRequest();
                req.responseType = "json";
                req.open("GET", getData.url, true);
                req.onload = function () {
                    var response = req.response;
                    getData.getAction(response);
                };
                req.send(null);
            } catch (e) {
                console.warn("Error : " + e);
            }
        } else {
            console.warn("Please Send An Object!");
        }
    }

    post(getData = {}) {
        if (typeof getData === "object") {
            try {
                /* code */
                var values = JSON.stringify(getData.body);
                var req = new XMLHttpRequest();
                req.responseType = "json";
                req.open("POST", getData.url, true);
                req.setRequestHeader(
                    "Content-Type",
                    "application/x-www-form-urlencoded"
                );

                req.onreadystatechange = () => {
                    if (
                        req.readyState === XMLHttpRequest.DONE &&
                        req.status === 200
                    ) {
                        var response = req.response;
                        getData.getAction(response);
                    }
                };
                req.send(values);
            } catch (e) {
                console.warn("Error : " + e);
            }
        } else {
            console.warn("Please Send An Object!");
        }
    }

    put(getData = {}) {
        if (typeof getData === "object") {
            try {
                /* code */
                var values = JSON.stringify(getData.body);
                var req = new XMLHttpRequest();
                req.responseType = "json";
                req.open("POST", getData.url, true);
                req.setRequestHeader(
                    "Content-Type",
                    "application/x-www-form-urlencoded"
                );

                req.onreadystatechange = () => {
                    if (
                        req.readyState === XMLHttpRequest.DONE &&
                        req.status === 200
                    ) {
                        var response = req.response;
                        getData.getAction(response);
                    }
                };
                req.send(values);
            } catch (e) {
                console.warn("Error : " + e);
            }
        } else {
            console.warn("Please Send An Object!");
        }
    }

    validateInputs(value) {
        if (typeof value === "string") {
            var badString = String("@#$_&-+()%|=[]<>{}*':;!?");
            for (var i = 0; i < badString.length; i++) {
                if (value.trim().includes(badString[i])) {
                    return true;
                }
            }
        } else {
            console.warn("Invalid Value String Allowed Only");
        }
    }
}

/* MAKING OBJECT FROM CLASS*/
export function Selector(tag){
  return document.querySelector(tag);
}
export var Request = new XHR();
//export {Request}  from "./xhr.js";

/******************************************
HOW TO USE 
*******************************************/
/*
import { Request } from "./xhr.js";

Request.post({
    url: "example.com/data",
    body: {
      formdata,
    },
    getAction: (data) => {
      console.log(data);
    },
  });
*/
