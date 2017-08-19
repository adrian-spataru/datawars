/* ============
 * Mutations for the account module
 * ============
 *
 * The mutations that are available on the
 * account module.
 */

import { STORE, CLEAR } from './mutation-types';

export default {
  [STORE](state, competition) {
    state.competitions.push(competition);
  },
  [CLEAR](state) {
    state.competitions = [];
  },

};
