<template>
  <div>
    <form @submit.prevent>
      <h4>Recognize</h4>
      <input
          type="file"
      >
      <input
          type="text"
          placeholder="Description"
          v-model="image.label"
      >
      <button @click="addPost">Publicate</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      image: {
        img: "",
        label: "",
        probability: "",
      }
    }
  },
  methods: {
    addPost() {
      this.post.id = Date.now();
      this.$emit("create", this.post);
      this.post = {
        title: "",
        body: "",
      }
  }

  }
}
</script>

<style scoped>

</style>