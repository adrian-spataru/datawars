import Vue from 'vue';
import store from './../../store';

// When the request succeeds
const success = (data) => {
  store.dispatch('competition/clear');
  data.forEach((d) => {
    store.dispatch('competition/store', d);
  });
};

// When the request fails
const failed = () => {
  // TODO:
};

export default () => {
  Vue.$http.get('/competitions')
    .then((response) => {
      console.log(response);
      if (!response.data) {
        console.log(response);
        failed();
      } else {
        success(response.data);
      }
    })
    .catch((error) => {
      console.log(error);
      failed();
    });
};
