const LOGIN = "LOGIN";
const LOGIN_SUCCESS = "LOGIN_SUCCESS";
const LOGOUT = "LOGOUT";
const LOGIN_FAIL = "LOGIN_FAIL";

import Vue from 'vue'

export default {
  state: {
    
    errorLogin: null,
    test: true,
    isLoggedIn: localStorage.getItem("token"),

    
  },
  mutations: {
    [LOGIN](state) {
      state.pending = true;
      state.errorLogin = false;

    },
    [LOGIN_SUCCESS](state) {
      state.isLoggedIn = true;
      state.pending = false;
      state.errorLogin = false;
    },
    [LOGIN_FAIL](state) {
      state.isLoggedIn = false;
      state.pending = false;
      state.errorLogin = true;
    },
    [LOGOUT](state) {
      state.isLoggedIn = false;
      state.errorLogin = false;

    }
  },
  actions: {
    login({
      state,
      commit,
      rootState
    }, creds) {
      console.log("login...", creds);
      commit(LOGIN); // show spinner
      Vue.http.post("/api/auth/login", creds).then(response =>  {
          localStorage.setItem("token", response.body.token);
          Vue.http.headers.common['Authorization'] = response.body.token
          commit(LOGIN_SUCCESS);


      },
        response => {

          commit(LOGIN_FAIL);


        }
      );

    },
    logout({
      commit
    }) {
      localStorage.removeItem("token");
      Vue.http.headers.common['Authorization'] = null
      commit(LOGOUT);
    }
  },
  getters: {
    isLoggedIn: state => {
      return state.isLoggedIn;
    }
  }
}