<template>
  <div class="container mx-auto mt-12">
    <div class="grid grid-cols-1 gap-6 mb-6 lg:grid-cols-3">
      <div class="w-full px-4 py-5">
        <div class="text-sm font-medium text-gray-500 truncate">
          <AudioPlayer />
          <div class="w-full px-4 py-5 bg-white rounded-lg shadow">
  
        
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import AudioPlayer from "@/components/AudioPlayer.vue";
// import axios from "axios";
export default {
  name: "AudioUpdateView",
  components: {
    AudioPlayer,
  },
};
//   data() {
//     return {
//       audioList: [],
//     };
//   },
//   mounted() {
//     this.getAudioList();
//   },
//   methods: {
//     getAudioList() {
//       axios
//         .get("/api")
//         .then((response) => {
//           console.log("data", response.data);
//           this.audioList = response.data;
//         })
//         .catch((error) => {
//           console.log("error", error);
//         });
//     },
//   },
// };
</script>
