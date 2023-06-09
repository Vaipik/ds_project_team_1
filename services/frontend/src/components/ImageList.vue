<template xmlns:x-on="http://www.w3.org/1999/xhtml">

  <div class="slider__content" x-ref="slider"
       x-on:scroll.debounce="$refs.slider.scrollLeft == 0 ? start = true : start = false; Math.abs(($refs.slider.scrollWidth - $refs.slider.offsetWidth) - $refs.slider.scrollLeft) < 5 ? end = true : end = false;">
    <image-item
        v-for="image in images"
        :image="image"
        v-bind:key="image.id"
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
.slider__content {
  overflow-x: scroll;
  -ms-scroll-snap-type: mandatory;
      scroll-snap-type: y ;
  display: flex;
  gap: 1rem;
  padding-bottom: 1rem;
  scrollbar-color: var(--scrollcolor) var(--scrollbackground);
}
.slider__content::-webkit-scrollbar {
  height: 0.5rem;
  width: 0.5rem;
  border-radius: 1rem;
  background: var(--scrollbackground);
}
.slider__content::-webkit-scrollbar-thumb {
  border-radius: 1rem;
  background: var(--scrollcolor);
}
.slider__content::-webkit-scrollbar-track {
  border-radius: 1rem;
  background: var(--scrollbackground);
}

</style>
