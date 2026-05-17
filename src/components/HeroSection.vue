<template>
  <section class="pt-32 pb-20 px-4 text-center">
    <div class="max-w-4xl mx-auto">

      <!-- Badge -->
      <div class="inline-flex items-center gap-2 bg-blue-600/10 border border-blue-500/20 text-blue-400 text-sm px-4 py-2 rounded-full mb-8">
        <span class="w-2 h-2 rounded-full bg-blue-400 animate-pulse"></span>
        Détection par Intelligence Artificielle
      </div>

      <!-- Titre -->
      <h1 class="text-5xl md:text-6xl font-bold text-white leading-tight mb-6">
        Diagnostic oculaire
        <span class="bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">
          instantané
        </span>
      </h1>

      <!-- Sous-titre -->
      <p class="text-gray-400 text-lg md:text-xl max-w-2xl mx-auto mb-12 leading-relaxed">
        Uploadez une rétinographie et notre modèle EfficientNetB0 détecte en quelques secondes
        parmi 4 pathologies oculaires avec <strong class="text-white">94% de précision</strong>.
      </p>

      <!-- Stats -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4 max-w-3xl mx-auto">
        <div v-for="stat in stats" :key="stat.label"
          class="bg-gray-900 border border-gray-800 rounded-2xl p-4">
          <div class="text-2xl font-bold text-white">{{ stat.value }}</div>
          <div class="text-gray-500 text-sm mt-1">{{ stat.label }}</div>
        </div>
      </div>

    </div>
  </section>
</template>

<script setup>
const stats = [
  { value: '94.16%', label: 'Précision' },
  { value: '99.11%', label: 'AUC Score' },
  { value: '4 217', label: 'Images entraînées' },
  { value: '4', label: 'Pathologies' },
]
</script>