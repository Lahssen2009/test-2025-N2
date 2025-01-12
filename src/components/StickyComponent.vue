<template>
  <div>
    <div style="height: 2000px; background: #f0f0f0;">
      <p>Scroll through the content above the sticky component.</p>
    </div>
    <StickyComponent /> <!-- Sticky at the bottom -->
  </div>
</template>

<script>
import StickyComponent from './StickyComponent.vue';

export default {
  components: {
    StickyComponent,
  },
};
</script>

<style>
/* Optional: Add app-wide styles */
</style>
