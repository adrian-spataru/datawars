import Vue from 'vue';
import store from './../../store';

// When the request succeeds
const success = () => {
  store.dispatch('auth/reseterror');
  Vue.router.push({
    name: 'login.index',
  });
};

// When the request fails
const failed = () => {
  store.dispatch('auth/error');
};

export default (user) => {
  Vue.$http.post('/auth/register', user)
    .then((response) => {
      if (response == null) {
        failed();
      } else {
        success();
      }
    })
    .catch(() => {
      failed();
    });
};
