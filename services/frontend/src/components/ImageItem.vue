<template>
  <div class="slider__item">
    <img class="slider__image"
         :src="image.img"
         alt="Whoops!">
    <div class="slider__info">
      <h2>This is {{ getArticle(image.label) }} {{ image.label }}</h2>
      <p class="probability">Probability: {{ image.probability }}%</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    image: {
      type: Object,
      required: true
    }
  },
  methods: {
    getArticle(label) {
      const vowels = ['a', 'e', 'i', 'o', 'u'];
      return vowels.includes(label.charAt(0).toLowerCase()) ? 'an' : 'a';
    }
  }
}
</script>

<style scoped>
.slider__item {
  scroll-snap-align: start;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  min-width: 120px;
  width: 160px;
  height: 240px;
  border-radius: 0.25rem;
  overflow: hidden;
  position: relative;
  aspect-ratio: 1;
}

@media (min-width: 460px) {
  .slider__item {
    aspect-ratio: 2/3;
    min-width: calc((100% / 2) - 2rem);
  }
}

@media (min-width: 940px) {
  .slider__item {
    min-width: calc((100% / 3) - 4rem);
  }
}

.slider__image {
  display: block;
  width: 100%;
  height: 100%;
  -o-object-fit: cover;
  object-fit: cover;
  position: absolute;
  top: 0;
  left: 0;
}

.slider__info {
  position: relative;
  padding: 4rem 2rem 2rem;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.75), rgba(32, 50, 57, 0));
}

.slider__info h2 {
  color: #fff;
  font-family: system-ui;
  line-height: 1.1;
  font-weight: 300;
  font-size: 1.75rem;
  margin: 0;
}

.probability {
  color: #fff;
  font-family: system-ui;
  font-size: 1rem;
  margin-top: 0.5rem;
}
</style>
