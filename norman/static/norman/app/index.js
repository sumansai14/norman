// Let javascript take over the world from here.
import jQuery from 'jquery';

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

jQuery.ajaxSetup({
  beforeSend: function(xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'););
    }
  }
});


import moment from 'moment';
import React from 'react';
import ReactDOM from 'react-dom';
import Reflux from 'reflux';
import * as Router from 'react-router';
import underscore from 'underscore';


export default{
  jQuery: jQuery,
  moment: moment,
  React: React,
  ReactDOM: ReactDOM,
  Reflux: Reflux,
  Router: Router,
  underscore: underscore,

  Norman: {
    routes: require('./routes').default,
  }
}
