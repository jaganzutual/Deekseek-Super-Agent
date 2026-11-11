<script setup>
import { computed, ref } from 'vue'
import trace from '../public/trace.json'
const index = ref(0)
const step = computed(() => trace[index.value])
const repo = import.meta.env.VITE_GITHUB_REPOSITORY || 'jaganzutual/Deekseek-Super-Agent'
const lines = { run: 'L28', scripted_model: 'L19', dispatch_tool: 'L13' }
const branch = import.meta.env.VITE_GITHUB_DEFAULT_BRANCH || 'master'
const codeUrl = computed(() => `https://github.com/${repo}/blob/${encodeURIComponent(branch)}/learn/examples/agent.py#${lines[step.value.code]}`)
const nodes = [{id:'user', name:'User'}, {id:'loop', name:'Agent loop + history'}, {id:'model', name:'Scripted model'}, {id:'tool', name:'Tool dispatcher'}]
function move(next) { index.value = Math.max(0, Math.min(trace.length - 1, next)) }
</script>
<template>
  <div class="walkthrough" @keydown.left.stop @keydown.right.stop @keydown.up.stop @keydown.down.stop>
    <div class="trace-top"><span>Step {{ index + 1 }} of {{ trace.length }}</span><strong aria-live="polite">{{ step.title }}</strong></div>
    <div class="trace-nodes" aria-label="Active component">
      <div v-for="node in nodes" :key="node.id" :class="['trace-node', { active: step.active === node.id }]">
        <small>{{ step.active === node.id ? 'Active' : ' ' }}</small><b>{{ node.name }}</b>
      </div>
    </div>
    <div class="trace-details" aria-live="polite">
      <div><small>Input</small><p>{{ step.input }}</p></div>
      <div><small>Output</small><p>{{ step.output }}</p></div>
      <div><small>History / state</small><p>{{ step.state }}</p></div>
    </div>
    <div class="trace-controls">
      <div class="buttons">
        <button type="button" :disabled="index === 0" @click="move(index - 1)">Previous step</button>
        <button type="button" class="primary" :disabled="index === trace.length - 1" @click="move(index + 1)">Next step</button>
        <button type="button" @click="move(0)">Reset</button>
      </div>
      <a :href="codeUrl" target="_blank" rel="noopener">View {{ step.code }} in Python ↗</a>
    </div>
  </div>
</template>
