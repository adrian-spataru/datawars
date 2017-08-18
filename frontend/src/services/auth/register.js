import Vue from 'vue';
import store from './../../store';

// When the request succeeds
const success = (token) => {
  store.dispatch('auth/login', token);
  Vue.router.push({
    name: 'home.index',
  });
};

// When the request fails
const failed = () => {
};

export default (user) => {
  if (!user.email || !user.password || !user.passwordConfirm || !user.firstName || !user.lastName) {
    failed();
  } else if (user.password !== user.passwordConfirm) {
    failed();
  } else {
    success('RandomGeneratedToken');
  }
};
