<template>
  <section id="result" class="py-16 px-4">
    <div class="max-w-2xl mx-auto">

      <h2 class="text-3xl font-bold text-white text-center mb-10">
        Résultat du diagnostic
      </h2>

      <!-- Carte résultat principal -->
      <div class="rounded-3xl p-8 mb-6 border"
        :class="diagnosticStyle.bg">

        <div class="flex items-center gap-4 mb-6">
          <div class="w-14 h-14 rounded-2xl flex items-center justify-center text-3xl"
            :class="diagnosticStyle.iconBg">
            {{ diagnosticStyle.icon }}
          </div>
          <div>
            <p class="text-gray-400 text-sm font-medium mb-1">Diagnostic détecté</p>
            <h3 class="text-2xl font-bold text-white">{{ diagnosticLabel }}</h3>
          </div>
          <div class="ml-auto text-right">
            <p class="text-gray-400 text-sm mb-1">Confiance</p>
            <p class="text-3xl font-bold" :class="diagnosticStyle.text">
              {{ result.confidence }}%
            </p>
          </div>
        </div>

        <!-- Barre de confiance -->
        <div class="w-full bg-gray-800 rounded-full h-2 mb-2">
          <div class="h-2 rounded-full transition-all duration-1000"
            :class="diagnosticStyle.bar"
            :style="{ width: result.confidence + '%' }">
          </div>
        </div>
        <p class="text-gray-500 text-xs">Niveau de confiance du modèle</p>
      </div>

      <!-- Probabilités par classe -->
      <div class="bg-gray-900 border border-gray-800 rounded-3xl p-6">
        <h4 class="text-white font-semibold mb-5">Probabilités par pathologie</h4>

        <div v-for="(prob, classe) in result.probabilites" :key="classe" class="mb-4">
          <div class="flex justify-between text-sm mb-1.5">
            <span class="text-gray-300 font-medium">{{ formatClasse(classe) }}</span>
            <span class="text-gray-400">{{ prob }}%</span>
          </div>
          <div class="w-full bg-gray-800 rounded-full h-1.5">
            <div class="h-1.5 rounded-full bg-blue-500 transition-all duration-700"
              :style="{ width: prob + '%' }">
            </div>
          </div>
        </div>
      </div>

      <!-- Avertissement médical -->
      <div class="mt-6 p-4 bg-yellow-500/10 border border-yellow-500/20 rounded-2xl flex gap-3">
        <span class="text-yellow-400 text-lg">⚠️</span>
        <p class="text-yellow-400/80 text-sm leading-relaxed">
          Ce diagnostic est généré par une IA et ne remplace pas l'avis d'un ophtalmologiste.
          Consultez un médecin pour toute décision médicale.
        </p>
      </div>

    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  result: Object
})

const labels = {
  cataract: 'Cataracte',
  diabetic_retinopathy: 'Rétinopathie diabétique',
  glaucoma: 'Glaucome',
  normal: 'Œil normal'
}

const diagnosticLabel = computed(() => labels[props.result.diagnostic] || props.result.diagnostic)

const styles = {
  normal: {
    bg: 'bg-green-500/10 border-green-500/30',
    iconBg: 'bg-green-500/20',
    icon: '✅',
    text: 'text-green-400',
    bar: 'bg-green-500'
  },
  cataract: {
    bg: 'bg-orange-500/10 border-orange-500/30',
    iconBg: 'bg-orange-500/20',
    icon: '🔶',
    text: 'text-orange-400',
    bar: 'bg-orange-500'
  },
  diabetic_retinopathy: {
    bg: 'bg-red-500/10 border-red-500/30',
    iconBg: 'bg-red-500/20',
    icon: '🔴',
    text: 'text-red-400',
    bar: 'bg-red-500'
  },
  glaucoma: {
    bg: 'bg-purple-500/10 border-purple-500/30',
    iconBg: 'bg-purple-500/20',
    icon: '🟣',
    text: 'text-purple-400',
    bar: 'bg-purple-500'
  }
}

const diagnosticStyle = computed(() => styles[props.result.diagnostic] || styles.normal)

function formatClasse(classe) {
  return labels[classe] || classe
}
</script>