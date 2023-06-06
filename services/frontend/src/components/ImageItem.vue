<template>
  <div class="image">
    <div>{{ image.img }}</div>
    <div>{{image.label }}</div>
    <div>Probability: <strong>{{ image.probability }}</strong></div>
  </div>
</template>


<script>
export default {
  props: {
    image: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>
.image {
  padding: 15px;
  border: 2px solid teal;
  margin-top: 15px;
}
</style>