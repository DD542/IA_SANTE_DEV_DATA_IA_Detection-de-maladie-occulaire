<template>
  <div class="min-h-screen bg-gray-950 text-white">
    <NavBar />
    <HeroSection />
    <UploadSection @result="showResult" />
    <ResultSection v-if="result" :result="result" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import NavBar from './components/NavBar.vue'
import HeroSection from './components/HeroSection.vue'
import UploadSection from './components/UploadSection.vue'
import ResultSection from './components/ResultSection.vue'

const result = ref(null)

function showResult(data) {
  result.value = data
}
</script>