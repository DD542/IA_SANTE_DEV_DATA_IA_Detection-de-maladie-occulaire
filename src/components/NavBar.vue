<template>
  <nav class="fixed top-0 left-0 right-0 z-50 bg-gray-950/90 backdrop-blur-md border-b border-gray-800">
    <div class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
      <!-- Logo -->
      <div class="flex items-center gap-3">
        <div class="w-9 h-9 rounded-xl bg-blue-600 flex items-center justify-center">
          <span class="text-white text-lg">👁</span>
        </div>
        <span class="text-white font-bold text-xl tracking-tight">OcularAI</span>
      </div>

      <!-- Links -->
      <div class="hidden md:flex items-center gap-8 text-gray-400 text-sm font-medium">
        <a href="#" class="hover:text-white transition">Accueil</a>
        <a href="#diagnostic" class="hover:text-white transition">Diagnostic</a>
        <a href="#" class="hover:text-white transition">À propos</a>
      </div>

      <!-- Badge -->
      <div class="bg-blue-600/20 border border-blue-500/30 text-blue-400 text-xs font-semibold px-3 py-1.5 rounded-full">
        IA · 94% précision
      </div>
    </div>
  </nav>
</template>