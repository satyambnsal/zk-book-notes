import { F1Field, Scalar } from 'ffjavascript'
import { wasm } from 'circom_tester'
import { describe, test, expect } from 'bun:test'
import path from 'path'

const p = Scalar.fromString("21888242871839275222246405745257275088548364400416034343698204186575808495617")
const Fr = new F1Field(p)
console.log(F1Field)


describe("All Binary", () => {
  test("Should work", async () => {
    const circuit = await wasm(path.join(__dirname, "../AllBinary/", "AllBinary.circom"));
    await circuit.loadConstraints();
    console.log("Circuit constraints", circuit.constraints.length)
    expect(circuit.constraints.length).toBe(4);
    const witness = await circuit.calculateWitness({ in: [0, 0, 0, 0] }, true)
    console.log(witness)
    expect(await circuit.calculateWitness({ in: [1, 0, 1, 1] })).toBeDefined()
    await expect(circuit.calculateWitness({ in: [1, 0, 1, 3] })).rejects.toThrow();
    // expect(true).toBe(true)
    // expect().toBeDefined()
  })
})
