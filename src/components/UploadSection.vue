<template>
  <section id="diagnostic" class="py-16 px-4">
    <div class="max-w-2xl mx-auto">

      <h2 class="text-3xl font-bold text-white text-center mb-3">
        Lancer un diagnostic
      </h2>
      <p class="text-gray-400 text-center mb-10">
        Formats acceptés : JPG, PNG · Taille max : 10MB
      </p>

      <!-- Zone upload -->
      <div
        @dragover.prevent
        @drop.prevent="handleDrop"
        @click="triggerInput"
        class="border-2 border-dashed border-gray-700 hover:border-blue-500 rounded-3xl p-12 text-center cursor-pointer transition-all duration-300 bg-gray-900 hover:bg-gray-900/80 group"
        :class="{ 'border-blue-500 bg-blue-500/5': isDragging }"
        @dragenter="isDragging = true"
        @dragleave="isDragging = false"
      >
        <!-- Preview image -->
        <div v-if="previewUrl" class="mb-6">
          <img :src="previewUrl" alt="Preview"
            class="w-48 h-48 object-cover rounded-2xl mx-auto border border-gray-700" />
        </div>

        <!-- Icône upload -->
        <div v-else class="w-16 h-16 bg-gray-800 rounded-2xl flex items-center justify-center mx-auto mb-4 group-hover:bg-blue-600/20 transition">
          <span class="text-3xl">📁</span>
        </div>

        <p class="text-white font-semibold text-lg mb-1">
          {{ previewUrl ? selectedFile.name : 'Glissez votre image ici' }}
        </p>
        <p class="text-gray-500 text-sm">
          {{ previewUrl ? 'Cliquez pour changer' : 'ou cliquez pour parcourir' }}
        </p>

        <input ref="inputRef" type="file" accept="image/*"
          class="hidden" @change="handleFileChange" />
      </div>

      <!-- Bouton analyser -->
      <button
        @click="analyze"
        :disabled="!selectedFile || loading"
        class="w-full mt-6 py-4 rounded-2xl font-bold text-lg transition-all duration-300
               bg-blue-600 hover:bg-blue-500 text-white
               disabled:opacity-40 disabled:cursor-not-allowed
               flex items-center justify-center gap-3"
      >
        <span v-if="loading" class="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin"></span>
        {{ loading ? 'Analyse en cours...' : 'Analyser l\'image' }}
      </button>

      <!-- Erreur -->
      <div v-if="error" class="mt-4 p-4 bg-red-500/10 border border-red-500/30 rounded-2xl text-red-400 text-sm text-center">
        {{ error }}
      </div>

    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const emit = defineEmits(['result'])

const inputRef    = ref(null)
const selectedFile = ref(null)
const previewUrl  = ref(null)
const loading     = ref(false)
const error       = ref(null)
const isDragging  = ref(false)

function triggerInput() {
  inputRef.value.click()
}

function handleFileChange(e) {
  const file = e.target.files[0]
  if (file) setFile(file)
}

function handleDrop(e) {
  isDragging.value = false
  const file = e.dataTransfer.files[0]
  if (file) setFile(file)
}

function setFile(file) {
  selectedFile.value = file
  previewUrl.value = URL.createObjectURL(file)
  error.value = null
  emit('result', null)
}

async function analyze() {
  if (!selectedFile.value) return

  loading.value = true
  error.value = null

  try {
    const formData = new FormData()
    formData.append('image', selectedFile.value)

    const response = await axios.post('http://127.0.0.1:5000/predict', formData)
    emit('result', response.data)

    // Scroll vers résultat
    setTimeout(() => {
      document.getElementById('result')?.scrollIntoView({ behavior: 'smooth' })
    }, 100)

  } catch (err) {
    error.value = "Erreur lors de l'analyse. Vérifiez que l'API Flask est active."
  } finally {
    loading.value = false
  }
}
</script>