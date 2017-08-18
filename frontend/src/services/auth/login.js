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
const failed = (error) => {
  console.log(error);
};

export default (user) => {
  Vue.$http.post('/auth/login', user)
    .then((response) => {
      success(response.data.token);
    })
    .catch((error) => {
      failed(error);
    });

  success('RandomGeneratedToken');
};
