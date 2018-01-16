package cmd

import (
    "github.com/spf13/cobra"
)


func NewTrackMyWorkCommand() *cobra.Command {

    cmd := &cobra.Command{
      Use:   "trackmywork",
      Short: "Track my work is an application to help you keep track of your tasks in a simple way using the command line.",
      Long: `Track my work
      A simple way to keep track of your tasks.
      Complete documentation is available at https://github.com/LucasMagnum/trackmywork`,
    }


    cmd.AddCommand(NewStartCommand())
    cmd.AddCommand(NewEditCommand())
    cmd.AddCommand(NewRegisterCommand())
    cmd.AddCommand(NewFinishCommand())

    cmd.AddCommand(NewShowCommand())
    cmd.AddCommand(NewClearCommand())

    return cmd
}
