/* ============
 * Mutations for the auth module
 * ============
 *
 * The mutations that are available on the
 * account module.
 */

import Vue from 'vue';
import {
  CHECK,
  LOGIN,
  LOGOUT,
  ERROR,
  RESETERROR,
} from './mutation-types';

export default {
  [CHECK](state) {
    state.authenticated = !!localStorage.getItem('id_token');
    if (state.authenticated) {
      Vue.$http.defaults.headers.common.Authorization = `${localStorage.getItem('id_token')}`;
    }
  },

  [LOGIN](state, token) {
    state.authenticated = true;
    state.error = false;
    localStorage.setItem('id_token', token);
    Vue.$http.defaults.headers.common.Authorization = `${token}`;
  },

  [LOGOUT](state) {
    state.authenticated = false;
    state.error = false;
    localStorage.removeItem('id_token');
    Vue.$http.defaults.headers.common.Authorization = '';
  },

  [ERROR](state) {
    state.error = true;
  },

  [RESETERROR](state) {
    state.error = false;
  },
};
