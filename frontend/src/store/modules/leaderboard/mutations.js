/* ============
 * Mutations for the account module
 * ============
 *
 * The mutations that are available on the
 * account module.
 */

import { STORE, CLEAR } from './mutation-types';

export default {
  [STORE](state, entry) {
    state.public.push(entry);
  },
  [CLEAR](state) {
    state.public = [];
  },

};
