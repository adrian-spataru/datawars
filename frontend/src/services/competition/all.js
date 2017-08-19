import Vue from 'vue';
import store from './../../store';

// When the request succeeds
const success = (data) => {
  store.dispatch('competition/store', data);
};

// When the request fails
const failed = () => {
  // TODO:
};

export default (id) => {
  Vue.$http.get(`/competition/${id}`)
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
