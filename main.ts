function calculateFrequencies (step: number) {
    f1 = ConcertA * twototheonetwelfth ** step
    basic.showNumber(f1)
}
input.onButtonPressed(Button.A, function () {
    step1 = step1 - 1
    basic.showArrow(ArrowNames.South)
    calculateFrequencies(step1)
})
input.onButtonPressed(Button.B, function () {
    step1 = step1 + 1
    basic.showArrow(ArrowNames.North)
    calculateFrequencies(step1)
})
input.onPinPressed(TouchPin.P1, function () {
    music.playTone(f1, music.beat(BeatFraction.Whole))
})
let f1 = 0
let twototheonetwelfth = 0
let ConcertA = 0
let step1 = 0
step1 = 0
ConcertA = 440
twototheonetwelfth = 1.05946309436
calculateFrequencies(step1)
basic.showIcon(IconNames.EigthNote)
