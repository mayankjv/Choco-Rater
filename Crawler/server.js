var express = require('express');
var fs      = require('fs');
var request = require('request');
var cheerio = require('cheerio');
var app     = express();


  var url = 'https://www.c-spot.com/chocolate-census/bars/';
  var barUrls = [];
  var chocolates = [];

  var promise1 = new Promise(function(resolve,reject) {
    console.log("in request2");
    request(url, function(error, response, html){
      if(!error){
        var $ = cheerio.load(html);
        var  i=0;
        $('tr').each(function(tr){
            if(i>1) {
                var children = $(this).children();
                var barUrl = children.eq(1).find('a').attr('href');
                var row = {
                    "Bar Name": children.eq(1).text().trim(),
                    "Maker": children.eq(2).text(),
                    "Country": children.eq(3).text(),
                    "Type" : children.eq(4).text(),
                    "Flavor" : children.eq(5).text(),
                    "Source" : children.eq(6).text(),
                    "Strain" : children.eq(7).text(),
                    "url" : barUrl,
                    "Type_More_Info" : "",
                    "Strain_More_Info" : "",
                    "Source_More_Info" : "",
                    "Flavor_More_Info" : "",
                    "Style" : ""
                };
                chocolates.push(row);
            }
            i++;
            resolve('Success!');
        })
      }
    });
    
  });
  promise1.then(function(resolve,reject) {
    console.log("in promise 2");
      for( var i=0; i<chocolates.length; i++) {
          request1(chocolates[i],i);
      }
  })
function request1(chocolate,idx) {
  var url2 = chocolate.url;
      var extra = []; 

    var promise2 = new Promise(function(resolve,reject) {
      request(url2, function(error, response, html) {
        if(error) reject(error);
        if(!error) {
            var $ = cheerio.load(html);
            var i=0;
            $('tr').each(function(tr){
             
              if(i>0) {
                 var children = $(this).children();
                  extra.push(children.eq(1).text().trim());
              }
              i++;
              resolve("Success");
            })
            chocolates[idx].Type_More_Info = extra[1];
            chocolates[idx].Strain_More_Info = extra[2];
            chocolates[idx].Source_More_Info = extra[3];
            chocolates[idx].Flavor_More_Info = extra[4];
            chocolates[idx].Style = extra[5];
            console.log(chocolates[idx]);
        }
      });
    });
      
}

