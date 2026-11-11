import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import Walkthrough from '../learn/components/Walkthrough.vue'
import trace from '../learn/public/trace.json'

describe('walkthrough', () => {
  it('replays every generated event and respects boundaries and reset', async () => {
    const view = mount(Walkthrough)
    const buttons = view.findAll('button')
    expect(buttons[0].attributes('disabled')).toBeDefined()
    for (let i = 0; i < trace.length; i++) {
      expect(view.text()).toContain(`Step ${i + 1} of ${trace.length}`)
      expect(view.text()).toContain(trace[i].title)
      expect(view.text()).toContain(trace[i].output)
      expect(view.find('.trace-node.active').text()).toContain('Active')
      if (i < trace.length - 1) await buttons[1].trigger('click')
    }
    expect(buttons[1].attributes('disabled')).toBeDefined()
    await buttons[0].trigger('click')
    expect(view.text()).toContain(`Step ${trace.length - 1} of ${trace.length}`)
    await buttons[2].trigger('click')
    expect(view.text()).toContain(`Step 1 of ${trace.length}`)
  })
  it('does not let arrow keys on the controls navigate the deck', async () => {
    const view = mount(Walkthrough, { attachTo: document.body })
    let reachedParent = false
    document.body.addEventListener('keydown', () => { reachedParent = true }, { once: true })
    await view.find('button').trigger('keydown', { key: 'ArrowRight' })
    expect(reachedParent).toBe(false)
    view.unmount()
  })
})
