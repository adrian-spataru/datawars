/* ============
 * Actions for the auth module
 * ============
 *
 * The actions that are available on the
 * auth module.
 */

import * as types from './mutation-types';

export const check = ({ commit }) => {
  commit(types.CHECK);
};

export const login = ({ commit }, payload) => {
  commit(types.LOGIN, payload);
};

export const logout = ({ commit }) => {
  commit(types.LOGOUT);
};

export const error = ({ commit }) => {
  commit(types.ERROR);
};

export const reseterror = ({ commit }) => {
  commit(types.RESETERROR);
};

export default {
  check,
  login,
  logout,
  error,
  reseterror,
};
