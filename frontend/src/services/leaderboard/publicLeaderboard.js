import Vue from 'vue';
import store from './../../store';

// When the request succeeds
const success = (data) => {
  store.dispatch('leaderboard/clear');
  data.forEach((d) => {
    store.dispatch('leaderboard/store', d);
  });
};

// When the request fails
const failed = () => {
  // TODO:
};

export default (compId) => {
  Vue.$http.get(`/competition/${compId}/public_leaderboard/`)
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
