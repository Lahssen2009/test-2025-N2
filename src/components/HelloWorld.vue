<template>
  <div class="container">
    <div class="card-list" @drop="onDrop" @dragover.prevent>
      <div
        v-for="(card, index) in cards"
        :key="card.id"
        class="card"
        draggable="true"
        @dragstart="startDrag(card, index)"
        :style="{ backgroundColor: card.color }"
      >
        {{ card.text }}
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { v4 as uuidv4 } from 'uuid';

export default {
  setup() {
    const cards = ref([]);
    const draggedCardIndex = ref(null);

    const randomTexts = [
      "TEXT1",
      "TEXT2",
      "TEXT3.",
      "TEXT4",
      "TEXT5",
      "TEXT6",
      "TEXT7",
      "TEXT8",
      "TEXT9",
      "TEXT10",
    ];

    const getRandomText = () => {
      return randomTexts[Math.floor(Math.random() * randomTexts.length)];
    };

    const getRandomColor = () => {
        const letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    };


    onMounted(() => {
      // Create initial cards with random text and colors
      for (let i = 0; i < 5; i++) {
        cards.value.push({ id: uuidv4(), text: getRandomText(), color: getRandomColor() });
      }
    });

    const startDrag = (card, index) => {
      draggedCardIndex.value = index;
    };

    const onDrop = (event) => {
      event.preventDefault(); // Prevent default drop behavior
      if (draggedCardIndex.value === null) return;

      const targetIndex = findDropIndex(event);
      if (targetIndex === null) return;

      const draggedCard = cards.value.splice(draggedCardIndex.value, 1)[0];
      cards.value.splice(targetIndex, 0, draggedCard);

      draggedCardIndex.value = null; // Reset dragged card index
    };

    const findDropIndex = (event) => {
      const cardElements = event.target.closest('.card-list').children;
      const mouseY = event.clientY;

      for (let i = 0; i < cardElements.length; i++) {
        const cardRect = cardElements[i].getBoundingClientRect();
        const cardCenterY = cardRect.top + cardRect.height / 2;

        if (mouseY < cardCenterY) {
          return i;
        }
      }

      return cardElements.length; // Drop at the end if mouse is below all cards
    };

    return {
      cards,
      startDrag,
      onDrop,
    };
  },
};
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh; /* Make sure the container takes up the full viewport height */
}

.card-list {
  display: flex;
  flex-direction: column;
  border: 1px solid #ccc;
  padding: 10px;
  min-width: 200px; /* Prevent shrinking too much */
}

.card {
  padding: 15px;
  margin-bottom: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  cursor: grab;
  user-select: none; /* Prevent text selection during drag */
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); /* Add a subtle shadow */
  transition: transform 0.2s; /* Add a smooth transition for drag feedback */
}

.card:hover {
  transform: scale(1.02); /* Slight scale on hover */
}

.card:active {
  cursor: grabbing;
  transform: scale(0.98);
}

.card.dragging { /* Style for the currently dragged card */
  opacity: 0.5;
  transform: scale(0.95);
}
</style>