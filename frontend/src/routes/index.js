/* ============
 * Routes File
 * ============
 *
 * The routes and redirects are defined in this file.
 */


/**
 * The routes
 *
 * @type {object} The routes
 */
export default [
  // Home
  {
    path: '/home',
    name: 'home.index',
    component: require('@/pages/home/index.vue'),

    // If the user needs to be authenticated to view this page
    meta: {
      auth: true,
    },
  },

  // Account
  {
    path: '/account',
    name: 'account.index',
    component: require('@/pages/account/index.vue'),

    // If the user needs to be authenticated to view this page
    meta: {
      auth: true,
    },
  },

  // Login
  {
    path: '/login',
    name: 'login.index',
    component: require('@/pages/login/index.vue'),

    // If the user needs to be a guest to view this page
    meta: {
      guest: true,
    },
  },
      // Leaderboard
  {
    path: '/leaderboard',
    name: 'leaderboard.index',
    component: require('@/pages/leaderboard/index.vue'),

    // If the user needs to be authenticated to view this page
    meta: {
      auth: true,
    },
  },
        // Competitions
  {
    path: '/competitions',
    name: 'competitions.index',
    component: require('@/pages/competitions/index.vue'),

    // If the user needs to be authenticated to view this page
    meta: {
      auth: true,
    },
  },
        // Competition
  {
    path: '/competition/:comp_id',
    name: 'competition.index',
    component: require('@/pages/competition/index.vue'),

    // If the user needs to be authenticated to view this page
    meta: {
      auth: true,
    },
  },
        // Leaderboard
  {
    path: '/competition/:comp_id/leaderboard',
    name: 'leaderboard.index',
    component: require('@/pages/leaderboard/index.vue'),

    // If the user needs to be authenticated to view this page
    meta: {
      auth: true,
    },
  },
        // Submission
  {
    path: '/competition/:comp_id/submission',
    name: 'submission.index',
    component: require('@/pages/submission/index.vue'),

    // If the user needs to be authenticated to view this page
    meta: {
      auth: true,
    },
  },
  // Register
  {
    path: '/register',
    name: 'register.index',
    component: require('@/pages/register/index.vue'),

    // If the user needs to be a guest to view this page
    meta: {
      guest: true,
    },
  },
  {
    path: '/',
    redirect: '/home',
  },
  {
    path: '/*',
    redirect: '/home',
  },


];
