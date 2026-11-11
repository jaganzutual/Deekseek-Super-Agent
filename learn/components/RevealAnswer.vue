<script setup>
import { ref } from 'vue'
const shown = ref(false)
</script>
<template>
  <div class="lesson-takeaway" @keydown.left.stop @keydown.right.stop>
    <button type="button" class="reveal-button" @click="shown = !shown">{{ shown ? 'Hide answer' : 'Reveal: what happens next?' }}</button>
    <span v-if="shown" role="status"> The loop adds the result to history and calls the model again.</span>
  </div>
</template>
