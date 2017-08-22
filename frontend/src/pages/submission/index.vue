<template lang="pug">
v-layout
    h1.ui.header Submission
    input(id="fileinput", type="file", @change="uploadFile").ui.button 
</template>
<script>
  /* ============
   * Home Index Page
   * ============
   *
   * The home index page.
   */
  import submissionService from '@/services/submission';


  export default {
    data() {
      return {
        file: {
          submission: null,
        },
      };
    },
    methods: {
      uploadFile() {
        const fileInput = document.getElementById('fileinput').files[0];
        if (fileInput) {
          const filePromise = new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onload = function onload() {
              resolve(reader.result);
            };
            reader.readAsText(fileInput);
            reader.onerror = reject;
          });
          filePromise.then((value) => {
            this.file.submission = value;
            console.log(this.file.submission);
            submissionService.upload(this.$route.params.comp_id, this.file);
          });
        }
      },
    },
    components: {
      VLayout: require('@/layouts/default.vue'),
    },
  };
</script>
