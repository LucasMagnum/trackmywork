package main


import (
    "fmt"
    "os"

    "github.com/lucasmagnum/trackmywork/pkg/trackmywork/cmd"
)

func main() {
    cmd := cmd.NewTrackMyWorkCommand()

    if err := cmd.Execute(); err != nil {
        fmt.Fprintf(os.Stderr, "error: %v\n", err)
        os.Exit(1)
    }

    os.Exit(0)
}
