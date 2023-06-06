<template>
  <div class="image" v-for="image in images" v-bind:key="image">
    <image-item
      v-for="image in images"
      :image="image"
      v-bind:key="image"
    />
  </div>
</template>

<script>
import ImageItem from "@/components/ImageItem.vue";
export default {
  components: {
    ImageItem,
  },
  props: {
    images: {
      type: Array,
      required: true,
    }
  }
}
</script>

<style scoped>

</style>