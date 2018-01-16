package cmd

import (
    "fmt"
    "strings"
    "github.com/spf13/cobra"
)


func NewStartCommand() *cobra.Command {

    cmd := &cobra.Command{
      Use:   "start",
      Short: "Start a new task",
      Run: func(cmd *cobra.Command, args []string) {
        fmt.Println("Start command yey!: " + strings.Join(args, " "))
      },
    }

    return cmd
}
