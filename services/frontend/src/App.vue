<template>
  <div>
    <h1 class="title">
      Object recognition
      <button class="help-button" @click="openModal">Help</button>
    </h1>
    <div class="slider" x-data="{start: true, end: false}">
      <image-list :images="images" @show-labels="showLabels" />
    </div>

    <div class="slider">
      <image-form @create="imagesList" :selected-cifar="cifar" @update="updateCifar" />
    </div>

    <div class="modal" v-if="isModalOpen" @click.self="closeModal">
      <div class="modal__content">
        <h2 class="modal__title">Object that can be recognized</h2>
        <ul class="modal__list">
          <li v-for="label in getCifarLabels" :key="label" class="modal__item">{{ label }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import ImageForm from "@/components/ImageForm.vue";
import ImageList from "@/components/ImageList.vue";

export default {
  components: {
    ImageForm,
    ImageList
  },
  data() {
    return {
      images: [],
      cifar10Labels: [
        'airplane',
        'automobile',
        'bird',
        'cat',
        'deer',
        'dog',
        'frog',
        'horse',
        'ship',
        'truck'
      ],
      cifar100Labels: [
        'apple', 'aquarium_fish', 'baby', 'bear', 'beaver', 'bed', 'bee', 'beetle', 'bicycle', 'bottle', 'bowl', 'boy', 'bridge', 'bus', 'butterfly',
        'camel', 'can', 'castle', 'caterpillar', 'cattle', 'chair', 'chimpanzee', 'clock', 'cloud', 'cockroach', 'couch', 'crab', 'crocodile', 'cup',
        'dinosaur', 'dolphin', 'elephant', 'flatfish', 'forest', 'fox', 'girl', 'hamster', 'house', 'kangaroo', 'computer_keyboard',
        'lamp', 'lawn_mower', 'leopard', 'lion', 'lizard', 'lobster', 'man', 'maple_tree', 'motorcycle', 'mountain', 'mouse', 'mushroom',
        'oak_tree', 'orange', 'orchid', 'otter', 'palm_tree', 'pear', 'pickup_truck', 'pine_tree', 'plain', 'plate', 'poppy', 'porcupine', 'possum',
        'rabbit', 'raccoon', 'ray', 'road', 'rocket', 'rose',
        'sea', 'seal', 'shark', 'shrew', 'skunk', 'skyscraper', 'snail', 'snake', 'spider', 'squirrel', 'streetcar', 'sunflower', 'sweet_pepper',
        'table', 'tank', 'telephone', 'television', 'tiger', 'tractor', 'train', 'trout', 'tulip', 'turtle',
        'wardrobe', 'whale', 'willow_tree', 'wolf', 'woman', 'worm'
      ],
      isModalOpen: false,
      cifar: 10
    };
  },
  methods: {
    imagesList(image) {
      this.images.push(image);
    },
    showLabels() {
      // No need to do anything here
    },
    openModal() {
      this.isModalOpen = true;
    },
    closeModal() {
      this.isModalOpen = false;
    },
    updateCifar(value) {
      this.cifar = value;
    }
  },
  computed: {
    getCifarLabels() {
      return this.cifar === 10 ? this.cifar10Labels : this.cifar100Labels;
    }
  }
};
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
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.help-button {
  background-color: transparent;
  color: #fff;
  border: 1px solid slategray;
  border-radius: 0.25rem;
  padding: 0.5rem 1rem;
  font-size: 1rem;
  cursor: pointer;
}

.slider {
  width: 85%;
  max-width: 1280px;
  margin: 0 auto;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal__content {
  background-color: transparent;
  padding: 2rem;
  border-radius: 0.25rem;
  max-height: 80vh;
  overflow-y: auto;
}

.modal__title {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 1rem;
  color: darkorange;
  position: sticky;
  top: 0;
  background-color: rgba(0, 0, 0, 0.7);
  padding: 0.5rem;
  z-index: 1;
}

.modal__list {
  list-style-type: none;
  justify-content: center;
  padding: 0;
  margin: 0;
}

.modal__item {
  margin-bottom: 0.5rem;
  color: white;
}

</style>
