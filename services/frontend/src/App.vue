<template>
  <div>
    <image-form
      @create="addPost"
    />
    <image-list
      :images="images"
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
      images: [
        {id: 1, title: "JavaScript", body: "Text body"},
        {id: 2, title: "JavaScript2", body: "Text body2"},
        {id: 3, title: "JavaScript3", body: "Text body3"},
      ],
      title: "",
      body: "",
    }
  },
  methods: {
    addPost(post) {
      this.posts.push(post)
    },
  },
}

</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
</style>