<script setup>
const repo = import.meta.env.VITE_GITHUB_REPOSITORY || 'jaganzutual/Deekseek-Super-Agent'
const lines = { run: 'L28', scripted_model: 'L19', dispatch_tool: 'L13' }
const branch = import.meta.env.VITE_GITHUB_DEFAULT_BRANCH || 'master'
const link = name => `https://github.com/${repo}/blob/${encodeURIComponent(branch)}/learn/examples/agent.py#${lines[name]}`
</script>
<template>
  <div class="boundary">
    <div class="boundary-node boundary-loop"><span>1</span><a :href="link('run')" target="_blank" rel="noopener">Agent loop + history ↗</a><p>Sends context, records messages, stops on a final answer.</p></div>
    <div class="boundary-paths">
      <div class="boundary-row"><div class="boundary-arrow">history →<br/>← request / answer</div><div class="boundary-node"><span>2</span><a :href="link('scripted_model')" target="_blank" rel="noopener">Scripted model ↗</a><p>Chooses a tool request or final response.</p></div></div>
      <div class="boundary-row"><div class="boundary-arrow">tool name →<br/>← note text</div><div class="boundary-node"><span>3</span><a :href="link('dispatch_tool')" target="_blank" rel="noopener">Tool dispatcher ↗</a><p>Runs the allowlisted read-only tool.</p></div></div>
    </div>
  </div>
</template>
