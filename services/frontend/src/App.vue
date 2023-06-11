<template>
  <h1 class="title">Object recognition</h1>
  <div class="slider" x-data="{start: true, end: false}">
    <image-list
        :images="images"
    />
  </div>

  <div class="slider">
      <image-form
          @create="imagesList"
      />
  </div>

</template>

<script>
import ImageForm from "@/components/ImageForm.vue";
import ImageList from "@/components/ImageList.vue";
export default {
  components: {
    ImageForm, ImageList
  },
  data() {
    return {
      images: [],
    }
  },
  methods: {
    imagesList(image) {
      this.images.push(image)
    },
  },
}

</script>

<style>
:root {
  --scrollcolor: #FF4500FF;
  --scrollbackground: #342121;
}

* {
  box-sizing: border-box;

}

html,
body {
  padding: 0;
  margin: 0;
}

body {
  background: #203239;
}

.title {
  font-size: 2.5rem;
  font-family: system-ui;
  line-height: 1.1;
  font-weight: 300;
  color: #fff;
  margin: 4rem auto 1rem;
  width: 85%;
  max-width: 1280px;
}

.slider {
  width: 85%;
  max-width: 1280px;
  margin: 0 auto;

}
</style>