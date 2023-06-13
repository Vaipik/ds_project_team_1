<template>
  <div class="modal-card">
    <form @submit.prevent="sendImage">
      <h4 v-if="errorMessage">{{ errorMessage }}</h4>
      <div class="input-container">
        <image-upload v-model="image.img"/>
      </div>
      <div class="progress-bar" v-if="isUploading">
        <div class="progress-fill" :style="{ width: progressPercentage }"></div>
      </div>
      <div class="button-container">
        <button type="submit" :disabled="isUploading">{{ isUploading ? 'Uploading...' : 'Recognize' }}</button>
      </div>
    </form>
  </div>
  <button class="change-cifar" @click="toggleCifar">Change to CIFAR-{{ cifar === 10 ? 100 : 10 }}</button>
</template>

<script>
import ImageUpload from "@/components/imageUpload.vue";
import axios from "axios";

export default {
  components: {ImageUpload},
  data() {
    return {
      image: {
        img: null,
        label: null,
        probability: null,
      },
      isUploading: false,
      progress: 0,
      errorMessage: null,
      cifar: 10,
      host: `http://213.159.251.140:28131/images/cifar/10`
    };
  },
  computed: {
    progressPercentage() {
      return `${Math.round(this.progress * 100)}%`;
    },
  },
  methods: {
    async sendImage() {
      try {
        this.isUploading = true;
        this.progress = 0;
        this.errorMessage = null;
        const formData = new FormData();
        formData.append("file", this.image.img);

        const response = await axios.post(
            `${this.host}`,
            formData,
            {
              headers: {
                "Content-Type": "multipart/form-data",
              },
              onUploadProgress: (progressEvent) => {
                this.progress = progressEvent.loaded / progressEvent.total;
              },
            }
        );

        const reader = new FileReader();
        reader.readAsDataURL(this.image.img);
        reader.onload = () => {
          this.image.id = Date.now();
          this.image.label = response.data.imageClass;
          this.image.probability = response.data.probability;
          this.image.img = reader.result;
          this.$emit("create", this.image);
          this.image = {
            img: null,
            label: null,
            probability: null,
          };
          this.isUploading = false;
          this.progress = 0;
        };

      } catch (e) {
        console.log(e);
        this.errorMessage = e.response.data.message
        this.isUploading = false;
        this.progress = 0;
      }
    },
    toggleCifar() {
      this.cifar = this.cifar === 10 ? 100 : 10;
      this.host = `http://213.159.251.140:28131/images/cifar/${this.cifar}`;
      this.$emit("update", this.cifar)
    }
  },
};
</script>

<style scoped>
.modal-card {
  width: 30%;
  margin: 10px auto;
  padding: 20px;
  background-color: transparent;
  border-radius: 10px;
  border: 2px solid orangered;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.modal-card h4 {
  margin: 0;
  text-align: center;
  position: relative;
  top: 100%;
  font-size: 14px;
  color: red;
}

.input-container {
  width: 100%;
  display: flex;
  justify-content: center;
}

.modal-card input[type="file"] {
  width: 100%;
  padding: 10px;
  background-color: #444;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.button-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.modal-card button {
  display: inline-block;
  padding: 12px 24px;
  background-color: transparent;
  color: #fff;
  border: none;
  border-radius: 10px;
  font-size: 16px;
  font-weight: normal;
  text-transform: uppercase;
  text-decoration: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.modal-card button:hover {
  background-color: darkorange;
}

.progress-bar {
  width: 100%;
  height: 10px;
  background-color: #555;
  border-radius: 5px;
  overflow: hidden;
  margin-top: 20px;
}

.progress-fill {
  width: 0;
  height: 100%;
  background-color: #4caf50;
  transition: width 0.3s ease-in-out;
}

.change-cifar {
  width: 30%; /* Adjust the width as desired */
  margin: 10px auto;
  padding: 10px;
  background-color: transparent;
  color: #fff;
  border: 2px solid orangered;
  border-radius: 10px;
  font-size: 16px;
  font-weight: normal;
  text-transform: uppercase;
  text-decoration: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
  display: block; /* Add this line */
  text-align: center; /* Add this line */
}

/* Media Queries */
@media (max-width: 768px) {
  .modal-card .change-cifar {
    width: 80%;
  }
}

@media (max-width: 480px) {
  .modal-card .change-cifar {
    width: 90%;
  }
}
</style>
