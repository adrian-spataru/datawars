<template lang="pug">
v-layout
  h1.ui.header Registration

</template>

<script>
  /* ============
   * Register Index Page
   * ============
   *
   * Page where the user can register.
   */

  import authService from '@/services/auth';

  export default {

    data() {
      return {
        user: {
          firstName: null,
          lastName: null,
          email: null,
          passwordConfirm: null,
          password: null,
        },
      };
    },

    methods: {
      register(user) {
        authService.register(user);
      },
    },

    components: {
      VLayout: require('@/layouts/default.vue'),

    },
  };
</script>
