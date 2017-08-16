// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import "semantic-ui-css/semantic.min.css"
import "./assets/style.css"
import VueResource from 'vue-resource'

import store from './store/index.js'

Vue.use(VueResource);
Vue.http.options.root = 'http://127.0.0.1:5000'

Vue.config.productionTip = false


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
