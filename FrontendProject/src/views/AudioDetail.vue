<template>
  <div class="container mx-auto mt-12">
    <div class="grid grid-cols-1 gap-6 mb-6 lg:grid-cols-3">
      <div class="w-full px-4 py-5">
        <div class="text-sm font-medium text-gray-500 truncate">
          <AudioPlayer src="{{audio.audio_file}}" />
          <div class="w-full px-4 py-5 bg-white rounded-lg shadow">
            <button
              class="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-cyan-500 to-blue-500 group-hover:from-cyan-500 group-hover:to-blue-500 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-cyan-200 dark:focus:ring-cyan-800"
            >
              <span
                class="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0"
              >
                Go Transcribe
              </span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="container mx-auto">
    <div class="flex flex-col">
      <div class="mb-8 w-full">
        <h4 class="px-2 text-xl font-bold text-navy-700 dark:text-white">
          General Information
        </h4>
        <p class="mt-2 px-2 text-base text-gray-600">
          {{ audio.description }}
        </p>
      </div>
      <div class="grid grid-cols-2 gap-4 px-2 w-full">
        <div
          class="flex flex-col items-start justify-center rounded-2xl bg-white bg-clip-border px-3 py-4 shadow-3xl shadow-shadow-500 dark:!bg-navy-700 dark:shadow-none"
        >
          <p class="text-sm text-gray-600">Customer</p>
          <p class="text-base font-medium text-navy-700 dark:text-white">
            {{ audio.customer }}
          </p>
        </div>

        <div
          class="flex flex-col justify-center rounded-2xl bg-white bg-clip-border px-3 py-4 shadow-3xl shadow-shadow-500 dark:!bg-navy-700 dark:shadow-none"
        >
          <p class="text-sm text-gray-600">Status</p>
          <p class="text-base font-medium text-navy-700 dark:text-white">
            {{ audio.status }}
          </p>
        </div>

        <div
          class="flex flex-col items-start justify-center rounded-2xl bg-white bg-clip-border px-3 py-4 shadow-3xl shadow-shadow-500 dark:!bg-navy-700 dark:shadow-none"
        >
          <p class="text-sm text-gray-600">Anatator</p>
          <p class="text-base font-medium text-navy-700 dark:text-white">
            {{ audio.user_name }}
          </p>
        </div>
      </div>
      <div class="grid grid-cols-2 gap-4 px-2 w-full">
        <div
          class="flex flex-col items-start justify-center rounded-2xl bg-white bg-clip-border px-3 py-4 shadow-3xl shadow-shadow-500 dark:!bg-navy-700 dark:shadow-none"
        >
          <p class="text-sm text-gray-600">Created</p>
          <p class="text-base font-medium text-navy-700 dark:text-white">
             {{ audio.timestamp }}
          </p>
        </div>

        <div
          class="flex flex-col justify-center rounded-2xl bg-white bg-clip-border px-3 py-4 shadow-3xl shadow-shadow-500 dark:!bg-navy-700 dark:shadow-none"
        >
          <p class="text-sm text-gray-600">Updated</p>
          <p class="text-base font-medium text-navy-700 dark:text-white">
            {{ audio.updated_at }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import AudioPlayer from "@/components/AudioPlayer.vue";
export default {
  name: "audiodetail",
  components: {
    AudioPlayer,
  },
  data() {
    return {
      audio: {},
    };
  },
  mounted() {
    this.getAudio();
  },
  methods: {
    async getAudio() {
      const id = this.$route.params.id;
      axios
        .get(`/api/${id}/`)
        .then((response) => {
          this.audio = response.data;
        })
        .catch((error) => console.log("error"));
    },
  },
};
</script>
