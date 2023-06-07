<template>
  <div>
    <form @submit.prevent="sendImage">
      <h4>Recognize</h4>
      <image-upload v-model="image.img"/>
      <button type="submit">Recognize</button>
    </form>
  </div>
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
      }
    }
  },
  methods: {
    async sendImage() {
      try {
        const response = await axios.post(
            "http://localhost:7001/images/",
            {
              file: this.image.img
            },
            {
              headers: {
                "Content-Type": "multipart/form-data"
              }
            }
        );
        const reader = new FileReader();
        reader.readAsDataURL(this.image.img);
        reader.onload = () => {
          this.image.id = Date.now()
          this.image.label = response.data.imageClass;
          this.image.img = reader.result;
          console.log(this.image)
          this.$emit("create", this.image);
          this.image = {
            img: null,
            label: null,
            probability: null,
          };
        };

        console.log("After all", this.image);
      } catch (e) {
        console.log(e)
      }


      // const reader = new FileReader();
      // reader.readAsDataURL(this.image.img);
      // reader.onload = () => {
      //   this.image.img = reader.result;

      // this.$emit("create", this.image);
      // this.image = {
      //   img: null,
      //   probability: null,
      //   label: null,
      // }
    }

  }
}
</script>

<style scoped>

</style>