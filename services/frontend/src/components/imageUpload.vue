<template>
  <label class="custom-file-input">
    <input type="file" @change="onChange($event)">
    <div class="file-info">
      <span class="file-name" ref="fileName">Choose File</span>
    </div>
  </label>
</template>

<script>
export default {
  props: ['modelValue'],
  methods: {
    onChange(event) {
      const file = event.target.files[0];
      const fileName = file ? file.name : '';

      this.$emit('update:modelValue', file);
      this.$refs.fileName.textContent = fileName;
    },
  },
};

</script>

<style scoped>
.custom-file-input {
  display: inline-block;
  position: relative;
  cursor: pointer;
  background-color: transparent;
  color: #fff;
  padding: 10px 20px;
  border-radius: 5px;
  transition: background-color 0.3s ease;
  border: 1px solid darkorange;
}

.custom-file-input:hover {
  background-color: #555;
}

.custom-file-input input[type="file"] {
  position: absolute;
  left: 0;
  top: 0;
  opacity: 0;
}

.custom-file-input .file-info {
  display: flex;
  align-items: center;
}

.custom-file-input {
  font-size: 20px;
  margin-right: 10px;
}

.custom-file-input .file-name {
  font-size: 14px;
  font-weight: normal;
}

.custom-file-input .file-name:before {
  content: "File: ";
</style>