import Vue from 'vue';

// When the request succeeds
const success = () => {
  Vue.router.push({
    name: 'home.index',
  });
};

// When the request fails
const failed = () => {
};

export default (id, submission) => {
  Vue.$http.post(`/competition/${id}/submission/`, submission)
    .then((response) => {
      console.log(response.status);
      if (!response.data.token) {
        console.log(response);
        failed();
      } else {
        success();
      }
    })
    .catch(() => {
      failed();
    });
};
