import Vue from 'vue';
// import store from './../../store';

// When the request succeeds
const success = () => {
  Vue.router.push({
    name: 'login.index',
  });
};

// When the request fails
const failed = () => {
};

export default (user) => {
  Vue.$http.post('/auth/register', user)
    .then((response) => {
      console.log(response);
      success();
    })
    .catch(() => {
      failed();
    });
};
