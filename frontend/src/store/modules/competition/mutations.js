/* ============
 * Mutations for the account module
 * ============
 *
 * The mutations that are available on the
 * account module.
 */

import { STORE } from './mutation-types';

export default {
  [STORE](state, competition) {
    state.id = competition.id;
    state.shortname = competition.shortname;
    state.name = competition.name;
    state.data = competition.data;
    state.description = competition.description;
    state.created_at = competition.created_at;
    state.ending_at = competition.ending_at;
  },
};
