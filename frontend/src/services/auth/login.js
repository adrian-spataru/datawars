import Vue from 'vue';
import accountService from './../account';
import store from './../../store';

// When the request succeeds
const success = (token) => {
  store.dispatch('auth/login', token);
  accountService.find();
  Vue.router.push({
    name: 'home.index',
  });
};

// When the request fails
const failed = () => {
  store.dispatch('auth/error');
};

export default (user) => {
  Vue.$http.post('/auth/login', user)
    .then((response) => {
      if (!response.data.token) {
        failed();
      } else {
        success(response.data.token);
        store.dispatch('auth/reseterror');
      }
    })
    .catch(() => {
      failed();
    });
};
