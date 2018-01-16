package cmd

import (
    "fmt"
    "strings"
    "github.com/spf13/cobra"
)


func NewFinishCommand() *cobra.Command {

    cmd := &cobra.Command{
      Use:   "finish",
      Short: "Finish a task",
      Run: func(cmd *cobra.Command, args []string) {
        fmt.Println("Finish command yey!: " + strings.Join(args, " "))
      },
    }

    return cmd
}
